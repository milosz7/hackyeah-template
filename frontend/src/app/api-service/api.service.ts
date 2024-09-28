import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class ApiService {

  private apiUrl = 'http://localhost:8080';

  constructor(private http: HttpClient) { }

  public getConversationHistory(): Observable<any> {
    return this.http.get(`${this.apiUrl}` + '/');
  }

  public getConversation(id: number): Observable<any> {
    return this.http.get(`${this.apiUrl}` + '/');
  }

  public postPrompt(text: string): Observable<any> {
    return this.http.post(`${this.apiUrl}` + '/', text);
  }

  public postCreateConversation(): Observable<any> {
    return this.http.post(`${this.apiUrl}` + '/', null);
  }
  
}
