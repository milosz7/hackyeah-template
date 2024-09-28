import { Conversation } from "../models/conversation"
import { Message, Sender } from "../models/message"

export const mockedConversations: Conversation[] = [
    {
        id: 0,
        date: new Date(),
        messages: []
    }
]

export const mockedMessages: Message[] = [
    {
        id: 0,
        date: new Date(),
        text: "siema eniu",
        sender: Sender.USER
    },
    {
        id: 0,
        date: new Date(),
        text: "na wałbrzych",
        sender: Sender.ADVISOR
    },
    {
        id: 0,
        date: new Date(),
        text: "siema eniu",
        sender: Sender.USER
    }

]
