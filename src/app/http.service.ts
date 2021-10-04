import { HttpClient } from  '@angular/common/http';
import { Injectable } from '@angular/core';
import { Game } from './game'

@Injectable({
  providedIn: 'root'
})
export class HttpService {

  constructor(private http: HttpClient) { }

  getGames(year: number) {
    return this.http.get<Game[]>(`/api/games?release_year=${year}`);
  }
}
