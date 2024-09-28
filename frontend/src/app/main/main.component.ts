import { CommonModule } from '@angular/common';
import { ChangeDetectionStrategy, Component } from '@angular/core';
import { FormComponent } from './form/form.component';
import { ConversationComponent } from './conversation/conversation.component';
import { SidebarComponent } from './sidebar/sidebar.component';

@Component({
    selector: 'app-main',
    standalone: true,
    imports: [
        CommonModule,
        FormComponent,
        ConversationComponent,
        SidebarComponent
    ],
    templateUrl: './main.component.html',
    styleUrl: './main.component.css',
    changeDetection: ChangeDetectionStrategy.OnPush,
})
export class MainComponent { }
