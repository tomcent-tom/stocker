import { Component, OnInit } from '@angular/core';
import { Transaction } from '../../assets/transaction';
import {FSMAService} from '../../services/fsma.service';

import { Observable } from 'rxjs/Observable';
import 'rxjs/add/operator/catch';
import 'rxjs/add/operator/map';

@Component({
  selector: 'fsma-feed',
  templateUrl: './feed.component.html',
  styleUrls: ['./feed.component.css']
})



export class FeedComponent implements OnInit {

  constructor(private fsmaService: FSMAService) { };
  transactions: Transaction[];
  errorMessage: string;

  ngOnInit(): void {
    this.getFeed();
  }

  getFeed() {
    this.fsmaService.getTransactions()
      .subscribe(
      transactions => this.transactions = transactions,
      error => this.errorMessage = <any>error);
  }

}