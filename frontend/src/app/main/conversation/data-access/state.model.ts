export interface promptAndAnswer {
    prompt: string;
    answer: string;
}

export interface ConversationStateModel {
    id: number;
    promptsAndAnswers: promptAndAnswer[];
  }