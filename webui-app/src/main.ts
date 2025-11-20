import { createApp } from 'vue'
import RpcService from "./jsonrpc.ts"
import type { IEventService } from './eventservice.ts'
import App from './App.vue'

function main() {
    createApp(App)
        .provide('IEventService', RpcService.resolve<IEventService>(/*TODO*/'IEventService')) 
        .mount('#app')
}

if (navigator.userAgent == 'pywebview') {
    window.addEventListener('pywebviewready', function () {
        main()
    })
}
else {
    main()
}
