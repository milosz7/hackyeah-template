export class GetConversationHistory {
    static readonly type = '[Conversation History] Get Conversation History';
}

export class SetConversationId {
    static readonly type = '[Conversation History] Set Conversation Id';

    constructor(public id: number) {}
}

export class Reset {
    static readonly type = '[Conversation History] Reset';
}