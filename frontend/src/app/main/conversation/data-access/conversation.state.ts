import { ApiService } from '../../../api-service/api.service';
import { Injectable } from "@angular/core";
import { Action, Selector, State, StateContext } from "@ngxs/store";
import { ConversationStateModel } from "./state.model";


@State<ConversationStateModel>({
    name: 'conversation',
    defaults: {
      id: 0,
        promptsAndAnswers: []
    },
  })
  @Injectable()
  export class ConversationState {

    constructor(private apiService: ApiService) {}

    @Selector()
    static getConversationId(state: ConversationStateModel): number {
      return state.id;
    }
  
    // @Action(FetchHistoryConversations)
    // fetchHistoryConversations(ctx: StateContext<ConversationStateModel>) {
    //   this.apiService.getData().

    //   ctx.setState({ count: state.count + 1 });
    // }
  }