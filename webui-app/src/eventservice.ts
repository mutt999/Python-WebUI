
export interface IEvent {
    id : number,
    name: string,
    participantCount: number
}

export type IEvents = IEvent[]

export interface IEventService {
    GetEvents(month: string): Promise<IEvents>
    AddEvent(name: string, count: number): Promise<IEvents>
    RemoveEvent(id: number): Promise<IEvents>
    UpdateEvent(event: IEvent): Promise<IEvents>
}

