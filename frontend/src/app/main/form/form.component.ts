import { CommonModule } from '@angular/common';
import { ChangeDetectionStrategy, Component } from '@angular/core';

@Component({
    selector: 'app-form',
    standalone: true,
    imports: [
        CommonModule,
    ],
    template: `<p>form works!</p>`,
    styleUrl: './form.component.css',
    changeDetection: ChangeDetectionStrategy.OnPush,
})
export class FormComponent { }
