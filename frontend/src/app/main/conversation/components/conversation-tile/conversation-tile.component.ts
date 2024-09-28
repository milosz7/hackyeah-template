import { CommonModule } from '@angular/common';
import { ChangeDetectionStrategy, Component, Input } from '@angular/core';

@Component({
    selector: 'app-conversation-tile',
    standalone: true,
    imports: [
        CommonModule,
    ],
    templateUrl: './conversation-tile.component.html',
    styleUrl: './conversation-tile.component.scss',
    changeDetection: ChangeDetectionStrategy.OnPush,
})
export class ConversationTileComponent {
    @Input()
    public text: string = '';
 }
