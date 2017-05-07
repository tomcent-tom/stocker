import { Injectable } from '@angular/core';
import { Http, Response, RequestOptions, Headers } from '@angular/http';
import { Observable } from 'rxjs/Observable';
import 'rxjs/add/operator/catch';
import 'rxjs/add/operator/map';
import { Transaction } from '../assets/transaction';

@Injectable()
export class FsmaService {
  private transactionUrl = 'http://localhost:5000/api/v1.0/defaultExcoList';

  constructor(private http: Http) { }

  getTransactions(): Observable<Transaction[]> {
    return this.http.get(this.transactionUrl)
      .map(this.extractData)
      .catch(this.handleError);
  }

  private extractData(res: Response) {
    let body = res.json();
    var result: Transaction[] = [];
    for (var trans of body) {
      let transit = new Transaction();
      transit.emittent = trans["Emittent"];
      transit.price = trans["Prijs"];
      transit.currency = trans["Munt"];
      transit.date = trans["Transactiedatum"];
      transit.kind = trans["Soort financieel instrument"];
      transit.name = trans["Naam meldplichtige"];
      transit.price = trans["Prijs"];
      transit.volume = trans["Aantal financiële instrumenten"];
      transit.total = trans["Totale bedrag"];
      result.push(transit);
    }
    return result || {};
  }

  private handleError(error: Response | any) {
    // In a real world app, you might use a remote logging infrastructure
    let errMsg: string;
    if (error instanceof Response) {
      const body = error.json() || '';
      const err = body.error || JSON.stringify(body);
      errMsg = `${error.status} - ${error.statusText || ''} ${err}`;
    } else {
      errMsg = error.message ? error.message : error.toString();
    }
    console.error(errMsg);
    return Observable.throw(errMsg);
  }
}
