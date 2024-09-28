import { CommonModule } from '@angular/common';
import { ChangeDetectionStrategy, Component, Input } from '@angular/core';
import { Conversation } from '../../models/conversation';

@Component({
    selector: 'app-conversation-history-list',
    standalone: true,
    imports: [
        CommonModule,
    ],
    template: `./conversation-history-list.component.html`,
    styleUrl: './conversation-history-list.component.css',
    changeDetection: ChangeDetectionStrategy.OnPush,
})
export class ConversationHistoryListComponent { 
    @Input() conversations: Conversation[];

    ngOnInit(): void {
      }
    
}
