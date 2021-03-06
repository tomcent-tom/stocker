import { Component, OnInit } from '@angular/core';
import { Transaction } from '../../assets/transaction';
import {FsmaService} from '../fsma.service';

import { Observable } from 'rxjs/Observable';
import 'rxjs/add/operator/catch';
import 'rxjs/add/operator/map';

@Component({
  selector: 'fsma-feed',
  templateUrl: './feed.component.html',
  styleUrls: ['./feed.component.css']
})
export class FeedComponent implements OnInit {

  constructor(private fsmaService: FsmaService) { };
  transactions: Transaction[];
  errorMessage: string;
  selectedTransaction: Transaction;

  ngOnInit(): void {
    this.getFeed();
  }

  onSelect(transaction: Transaction): void {
    this.selectedTransaction = transaction;
  }

  getFeed() {
    this.fsmaService.getTransactions()
      .subscribe(
      transactions => this.transactions = transactions,
      error => this.errorMessage = <any>error);
  }

}
