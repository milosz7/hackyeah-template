import { CommonModule } from '@angular/common';
import { ChangeDetectionStrategy, Component } from '@angular/core';
import { ConversationHistoryListComponent } from '../conversation-history-list/conversation-history-list.component';
@Component({
    selector: 'app-sidebar',
    standalone: true,
    imports: [
        CommonModule,
        ConversationHistoryListComponent
    ],
    template: `<app-conversation-history-list/>`,
    styleUrl: './sidebar.component.css',
    changeDetection: ChangeDetectionStrategy.OnPush,
})
export class SidebarComponent { }
