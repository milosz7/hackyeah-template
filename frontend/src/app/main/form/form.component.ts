import { CommonModule } from '@angular/common';
import { ChangeDetectionStrategy, Component } from '@angular/core';

@Component({
    selector: 'app-form',
    standalone: true,
    imports: [
        CommonModule,
    ],
    templateUrl: './form.component.html',
    styleUrl: './form.component.scss',
    changeDetection: ChangeDetectionStrategy.OnPush,
})
export class FormComponent { }
