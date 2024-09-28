import { Message } from "./message"
export interface Conversation {
    id: number;
    date: Date;
    messages: Message[];
}