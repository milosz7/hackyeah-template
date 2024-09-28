import { CommonModule } from '@angular/common';
import { ChangeDetectionStrategy, Component, Input } from '@angular/core';
import { Message, Sender } from '../../../../models/message';

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
    @Input()
    public message: Message|any;
    
    public isAdvisor: Boolean = false;

    ngOnInit() : void {
        if(this.message){
        this.isAdvisor = this.message.sender == Sender.ADVISOR;
        }
    }


 }
