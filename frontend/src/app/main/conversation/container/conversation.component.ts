import { CommonModule } from '@angular/common';
import { ChangeDetectionStrategy, Component } from '@angular/core';
import { ConversationTileComponent } from '../components/conversation-tile/conversation-tile.component';
import { Message, Sender } from '../../../models/message';
import { mockedMessages } from '../../../data/mockConversationList'

@Component({
    selector: 'app-conversation',
    standalone: true,
    imports: [
        CommonModule,
        ConversationTileComponent,
    ],
    templateUrl: './conversation.component.html',
    styleUrl: './conversation.component.scss',
    changeDetection: ChangeDetectionStrategy.OnPush,
})
export class ConversationComponent { 
    public text: string = "Oto nowy tekst w tym dymku";
    public messages = mockedMessages;
}
