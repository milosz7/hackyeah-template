import { Injectable } from "@angular/core";
import { Action, Selector, State, StateContext } from "@ngxs/store";
import { tap } from "rxjs/operators";
import { ApiService } from '../../../api-service/api.service';
import { ConversationStateModel } from "./models/conversation.state-model";
import { Message } from '../../../models/message';
import { CreateConversation, GetConversation, PostPrompt } from './conversation.actions';


@State<ConversationStateModel>({
    name: 'conversation',
    defaults: {
      id: 0,
      date: new Date(),
      messages: []
    },
  })
  @Injectable()
  export class ConversationState {

    constructor(private apiService: ApiService) {}

    @Selector()
    static getConversationId(state: ConversationStateModel): number {
      return state.id;
    }

    @Selector()
    static getConversationMessages(state: ConversationStateModel): Message[] {
      return state.messages;
    }
  
    @Action(GetConversation)
    getConversation(ctx: StateContext<ConversationStateModel>, action: GetConversation): any {
      return this.apiService.getConversation(action.id).pipe(
        tap((response) => {
          ctx.patchState({ id: response.id, date: response.date, messages: response.messages });
        })
      );
    }

    @Action(PostPrompt)
    postPrompt(ctx: StateContext<ConversationStateModel>, action: PostPrompt): any {
      return this.apiService.postPrompt(action.text);
    }

    @Action(CreateConversation)
    createConversation(ctx: StateContext<ConversationStateModel>) : any {
      return this.apiService.postCreateConversation().pipe(
        tap((response) => {
          ctx.patchState({ id: response.id });
        })
      );
    }
  }