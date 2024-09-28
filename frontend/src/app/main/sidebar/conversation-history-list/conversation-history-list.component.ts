import { CommonModule } from '@angular/common';
import { ChangeDetectionStrategy, Component, Input } from '@angular/core';
import { Conversation } from '../../../models/conversation';
import { mockedConversations } from '../../../data/mockConversationList'

@Component({
    selector: 'app-conversation-history-list',
    standalone: true,
    imports: [
        CommonModule,
    ],
    templateUrl: `./conversation-history-list.html`,
    styleUrl: './conversation-history-list.component.css',
    changeDetection: ChangeDetectionStrategy.OnPush,
})
export class ConversationHistoryListComponent { 
    formatDate(date: Date): string {
        const day = ('0' + date.getDate()).slice(-2);
        const month = ('0' + (date.getMonth() + 1)).slice(-2); // Add 1 because months are zero-indexed
        const year = date.getFullYear();

        return `${day}-${month}-${year}`;
      }
    conversations: Conversation[] = mockedConversations;

    ngOnInit(): void {

      }
    
}
