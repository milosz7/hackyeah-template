import { Component } from '@angular/core';
import { RouterOutlet } from '@angular/router';
import { HttpClientModule } from '@angular/common/http';
import { ApiService } from './services/api.service';
import { MainComponent } from './main/main.component';
import { HeaderComponent } from './header/header.component';
import { FooterComponent } from './footer/footer.component';


@Component({
  selector: 'app-root',
  standalone: true,
  imports: [RouterOutlet, HttpClientModule, MainComponent, HeaderComponent, FooterComponent],
  templateUrl: './app.component.html',
  styleUrl: './app.component.scss'
})
export class AppComponent {
  title = 'my-angular-app';
  public data: any;

  constructor(private apiService: ApiService) {}

  ngOnInit(): void {
    this.apiService.getData().subscribe(
      (response: any) =>  {
        this.data = response.data;
      },
      (error: any) => {
        console.error('Error fetching data', error);
      }
    )
  }
}
