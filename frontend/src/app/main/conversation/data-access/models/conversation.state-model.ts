import { Message } from "../../../../models/message"

export interface ConversationStateModel {
    id: number;
    date: Date;
    messages: Message[];
}