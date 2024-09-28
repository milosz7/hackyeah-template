export class GetConversation {
    static readonly type = '[Conversation] Get Conversation';

    constructor(public id: number) {}
}

export class PostPrompt {
    static readonly type = '[Conversation] Post Prompt';

    constructor(public text: string) {}
}

export class CreateConversation {
    static readonly type = '[Conversation] Create Conversation';
}

export class Reset {
    static readonly type = '[Conversation] Reset';
}

