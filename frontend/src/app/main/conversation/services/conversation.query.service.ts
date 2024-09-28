import { Injectable } from '@angular/core';
import { Store } from '@ngxs/store';
import { Observable } from 'rxjs';
import { ConversationState } from '../data-access/conversation.state';
import { Message } from '../../../models/message';

@Injectable({
  providedIn: 'root'
})
export class ConversationQueryService {

  public messages$: Observable<Message[]>;
  
  constructor(private store: Store) {
    this.messages$ = this.store.select(ConversationState.getConversationMessages)
  }

}
