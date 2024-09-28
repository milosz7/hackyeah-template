import { Injectable } from '@angular/core';
import { Store } from '@ngxs/store';
import { Observable } from 'rxjs';
import { ConversationState } from '../data-access/conversation.state';
import { Message } from '../../../models/message';
import { CreateConversation, PostPrompt } from '../data-access/conversation.actions';

@Injectable({
  providedIn: 'root'
})
export class ConversationPresenterService {
  
  constructor(private store: Store) {}

  public sendPrompt(promptText: string): Observable<any> {
    return this.store.dispatch(new PostPrompt(promptText));
  }

  public createConversation(): Observable<any> {
    return this.store.dispatch(new CreateConversation());
  }

}