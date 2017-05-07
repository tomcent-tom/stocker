import { Component, OnInit } from '@angular/core';
import {Purchase} from '../../assets/purchase';
import {Portfolio} from '../../assets/portfolio';
import {SdbService} from '../sdb.service';

@Component({
  selector: 'app-portfolio',
  templateUrl: './portfolio.component.html',
  styleUrls: ['./portfolio.component.css']
})
export class PortfolioComponent implements OnInit {
  portfolio: Portfolio;
  purchases: Purchase[];
  errorMessage: string;
  constructor(private sdbService: SdbService) { }

// TODO: to change 1
  ngOnInit() {
    this.getPortfolio(1);
    this.getPurchases(1);
  }

  getPortfolio(id) {
    this.sdbService.getPortfolio(id)
      .subscribe(
      Portfolio => this.portfolio = Portfolio,
      error => this.errorMessage = <any>error);
  }

  getPurchases(id) {
    this.sdbService.getPurchases(id)
      .subscribe(
      Purchases => this.purchases = Purchases,
      error => this.errorMessage = <any>error);
  }

}
