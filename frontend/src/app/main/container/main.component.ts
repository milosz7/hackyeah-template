import { CommonModule } from '@angular/common';
import { ChangeDetectionStrategy, Component } from '@angular/core';
import { FormComponent } from '../form/form.component';
import { SidebarComponent } from '../sidebar/container/sidebar.component';
import { ConversationComponent } from '../conversation/container/conversation.component';

@Component({
    selector: 'app-main',
    standalone: true,
    imports: [
        CommonModule,
        FormComponent,
        SidebarComponent,
        ConversationComponent
    ],
    templateUrl: './main.component.html',
    styleUrl: './main.component.scss',
    changeDetection: ChangeDetectionStrategy.OnPush,
})
export class MainComponent { }
