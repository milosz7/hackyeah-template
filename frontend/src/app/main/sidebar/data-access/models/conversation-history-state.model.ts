import { ConversationListItem } from '../../../../models/conversation-list-item.model';

export interface ConversationHistoryStateModel {
    selectedConversationId: number;
    conversationHistoryListItems: ConversationListItem[];
}