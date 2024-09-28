import { GetConversationHistory } from './../../data-access/conversation-history.actions';
import { Injectable } from '@angular/core';
import { Store } from '@ngxs/store';
import { Observable } from 'rxjs';
import { ConversationListItem } from '../../../../models/conversation-list-item.model';
import { ConversationHistoryState } from '../../data-access/conversation-history.state';
import { ApiService } from '../../../../api-service/api.service';

@Injectable({
  providedIn: 'root'
})
export class ConversationHistoryQueryService {

  public conversationHistoryListItems$: Observable<ConversationListItem[]>;
  
  constructor(private store: Store, private apiService: ApiService) {
    this.conversationHistoryListItems$ = this.store.select(ConversationHistoryState.getConversationHistoryItems);
    // this.conversationHistoryListItems$ = this.apiService.getConversationHistory();
  }

  public fetchConversation(): void {
    this.store.dispatch(new GetConversationHistory());
  }

}