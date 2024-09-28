import { CommonModule } from '@angular/common';
import { ChangeDetectionStrategy, Component, Input } from '@angular/core';
import { Store } from '@ngxs/store';
import { Observable } from 'rxjs';
import { ConversationListItem } from '../../../models/conversation-list-item.model';
import { mockedConversations } from '../../../data/mockConversationList'
import { ConversationHistoryQueryService } from './services/conversation-history.query';

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
  
    public conversations$: Observable<ConversationListItem[]>;

    constructor(private query: ConversationHistoryQueryService) {
      this.query.fetchConversation();
      this.conversations$ = this.query.conversationHistoryListItems$;
    }

    formatDate(date: Date): string {
      const day = ('0' + date.getDate()).slice(-2);
      const month = ('0' + (date.getMonth() + 1)).slice(-2); // Add 1 because months are zero-indexed
      const year = date.getFullYear();

      return `${day}-${month}-${year}`;
    }
}
