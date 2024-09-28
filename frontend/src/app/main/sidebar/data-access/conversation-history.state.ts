import { Injectable } from "@angular/core";
import { Action, Selector, State, StateContext } from "@ngxs/store";
import { tap } from "rxjs/operators";
import { ApiService } from '../../../api-service/api.service';
import { ConversationHistoryStateModel } from "./models/conversation-history-state.model";
import { GetConversationHistory, SetConversationId } from './conversation-history.actions';
import { ConversationListItem } from "../../../models/conversation-list-item.model";


@State<ConversationHistoryStateModel>({
    name: 'conversationHistory',
    defaults: {
      selectedConversationId: 0,
      conversationHistoryListItems: []
    },
  })
  @Injectable()
  export class ConversationHistoryState {

    constructor(private apiService: ApiService) {}

    @Selector()
    static getConversationHistoryItems(state: ConversationHistoryStateModel): ConversationListItem[] {
      return state.conversationHistoryListItems;
    }

    @Selector()
    static getCurrentConversationId(state: ConversationHistoryStateModel): number {
      return state.selectedConversationId;
    }
  
    @Action(GetConversationHistory)
    getConversationHistory(ctx: StateContext<ConversationHistoryStateModel>): any {
      return this.apiService.getConversationHistory().pipe(
        tap((response) => {
          ctx.patchState({ conversationHistoryListItems: response.items });
        })
      );
    }

    @Action(SetConversationId)
    selectConversationId(ctx: StateContext<ConversationHistoryStateModel>, action: SetConversationId): any {
      ctx.patchState({ selectedConversationId: action.id})
    }
  }