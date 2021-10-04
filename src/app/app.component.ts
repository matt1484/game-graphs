import { Component, OnInit } from '@angular/core';
import { HttpService } from './http.service';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss']
})
export class AppComponent implements OnInit {
  title = 'game-graphs';
  cols: number = 12;
  genreByPlatformSeries: any[] = [];
  top10Games: { name: string; sales: number; }[] = [];
  totalSales: number = 0;
  totalGames: number = 0;
  totalPublishers: number = 0;
  platformDistribution: any[] = [];
  year: number = 2016;

  constructor(private httpService: HttpService) {}

  ngOnInit() {
    this.reloadData();
    this.calcCols();
  }

  calcCols() {
    this.cols = Math.max(Math.floor(Math.min(Math.floor(window.innerWidth / 120), 12)/2) * 2, 1);
  }

  reloadData() {
    this.httpService.getGames(this.year).subscribe(
      (response) => { 
        const genreByPlatformSeries: { name: string; series: { name: string; value: number; }[] }[] = [];
        const genreToIndex: { [key: string]: number } = {};
        let totalSales: number = 0;
        let totalGames: number = 0;
        let top10Games: { name: string; sales: number; }[] = [];
        const allPublishers: Set<string> = new Set<string>();
        const platformToIndex: { [key: string]: number } = {};
        const platformDistribution: { name: string; value: number; }[] = [];

        response.forEach((game) => {
          const sales: number = Math.round((game.eu_sales + game.jp_sales + game.na_sales + game.other_sales + Number.EPSILON) * 100) / 100;
          totalSales += sales;
          totalGames += 1;
          allPublishers.add(game.publisher);
          let index = top10Games.length;
          for (index = top10Games.length; index > 0 && sales > top10Games[index-1].sales; index--) {}
          if (index < 10) {
            top10Games.splice(index, 0, {name: game.title, sales: sales});
          }
          top10Games = top10Games.slice(0, 10);

          if (genreToIndex[game.genre] === undefined) {
            genreToIndex[game.genre] = genreByPlatformSeries.length;
            genreByPlatformSeries.push({
              name: game.genre,
              series: [
                { name: 'Europe', value: 0},
                { name: 'Japan', value: 0},
                { name: 'North America', value: 0},
                { name: 'Other', value: 0},
              ],
            });
          }
          genreByPlatformSeries[genreToIndex[game.genre]].series[0].value += game.eu_sales;
          genreByPlatformSeries[genreToIndex[game.genre]].series[1].value += game.jp_sales;
          genreByPlatformSeries[genreToIndex[game.genre]].series[2].value += game.na_sales;
          genreByPlatformSeries[genreToIndex[game.genre]].series[3].value += game.other_sales;

          if (platformToIndex[game.platform] === undefined) {
            platformToIndex[game.platform] = platformDistribution.length;
            platformDistribution.push({
              name: game.platform,
              value: 0,
            });
          }
          platformDistribution[platformToIndex[game.platform]].value += sales;
        });
        
        this.genreByPlatformSeries = genreByPlatformSeries;
        this.top10Games = top10Games;
        this.totalGames = totalGames;
        this.totalPublishers = allPublishers.size;
        this.totalSales = totalSales;
        this.platformDistribution = platformDistribution;
      },
      (error) => { console.log(error); });
  }
}
