export interface Message {
    id: number;
    date: Date;
    text: String;
    sender: Sender;
}

export enum Sender {
    USER = 'USER',
    ADVISOR = 'ADVISOR'
}