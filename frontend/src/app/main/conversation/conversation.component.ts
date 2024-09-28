import { CommonModule } from '@angular/common';
import { ChangeDetectionStrategy, Component } from '@angular/core';

@Component({
    selector: 'app-conversation',
    standalone: true,
    imports: [
        CommonModule,
    ],
    template: `<p>conversation works!</p>`,
    styleUrl: './conversation.component.css',
    changeDetection: ChangeDetectionStrategy.OnPush,
})
export class ConversationComponent { }
