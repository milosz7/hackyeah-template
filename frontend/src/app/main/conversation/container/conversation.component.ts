import { CommonModule } from '@angular/common';
import { ChangeDetectionStrategy, Component } from '@angular/core';
import { ConversationTileComponent } from '../conversation-tile/conversation-tile.component';

@Component({
    selector: 'app-conversation',
    standalone: true,
    imports: [
        CommonModule,
        ConversationTileComponent
    ],
    templateUrl: './conversation.component.html',
    styleUrl: './conversation.component.scss',
    changeDetection: ChangeDetectionStrategy.OnPush,
})
export class ConversationComponent { 
    public text: string = "Oto nowy tekst w tym dymku";
}
