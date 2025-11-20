
type RpcRemoteCall = {
    ClassName: string,
    MethodName: string,
    ArgumentsAsJsonString: string
}

type RpcRemoteCallFunc = (rpcCall: RpcRemoteCall) => Promise<string>
type RpcRemoteHandleRequestFunc = (rpcCall: string) => Promise<string>

type RpcRemoteApi = {
    api: { HandleRequest: RpcRemoteHandleRequestFunc; };
};

declare global {
    type ChromeWebViewHostObjectsApi = {
        webview: { hostObjects: RpcRemoteApi }
    }
    var chrome: ChromeWebViewHostObjectsApi;
    var pywebview: RpcRemoteApi;
}

class RpcService {

    private static instance: RpcService

    private remoteCall: RpcRemoteCallFunc

    public constructor() {
        if (RpcService.instance) {
            throw new Error("This is a singleton. New instance cannot be created.");
        }
        RpcService.instance = this;
        switch (navigator.userAgent) {
            case 'pywebview':
                this.remoteCall = this.pythonWebViewCall
                break
            case 'dotnetwebview':
                this.remoteCall = this.dotNetWebViewCall
                break
            default:
                this.remoteCall = this.httpServerCall
                break
        }
    }

    private async pythonWebViewCall(rpcCall: RpcRemoteCall) {
        const json = await pywebview.api.HandleRequest(JSON.stringify(rpcCall))
        return JSON.parse(json)
    }

    private async dotNetWebViewCall(rpcCall: RpcRemoteCall) {
        const api = chrome.webview.hostObjects.api;
        const json = await api.HandleRequest(JSON.stringify(rpcCall))
        return JSON.parse(json)
    }

    private async httpServerCall(rpcCall: RpcRemoteCall) {
        const response = await fetch('http://localhost:9000/HandleRequest', {
            method: "POST",
            body: JSON.stringify(rpcCall),
            headers: { "Content-type": "application/json; charset=UTF-8" }
        });
        if (response.ok) {
            return await response.json();
        }
    }

    public resolve<T extends object>(serviceName: string): T {
        class RpcProxyHandler<T extends object> implements ProxyHandler<T> {
            constructor(private rpcService: RpcService, private serviceName: string) {}
            get(_: T, property: string, __: any) {
                const self = this
                return async function (...args: any[]) {
                    const methodName = property
                    const className = self.serviceName
                    return await self.rpcService.remoteCall({
                        'ClassName': className,
                        'MethodName': methodName,
                        'ArgumentsAsJsonString': JSON.stringify(Array.from(args))
                    })
                }
            }
        }
        return new Proxy({} as T, new RpcProxyHandler<T>(this,serviceName)) as T;
    }
}

let rpcServiceInstance = Object.freeze(new RpcService());

export default rpcServiceInstance;
