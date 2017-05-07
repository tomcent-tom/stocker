import { Injectable } from '@angular/core';
import { Http, Response, RequestOptions, Headers } from '@angular/http';
import { Observable } from 'rxjs/Observable';

import 'rxjs/add/operator/catch';
import 'rxjs/add/operator/map';

import { Purchase } from '../assets/purchase';
import { Portfolio } from '../assets/portfolio';

@Injectable()
export class SdbService {
  private baseUrl = 'http://localhost:5000/api/v1.0';
  constructor(private http: Http) { }

  getPortfolio(portfolioId): Observable<Portfolio> {
    return this.http.get(this.baseUrl + '/portfolio/' + portfolioId)
      .map(this.mapPortfolio)
      .catch(this.handleError);
  }

  private mapPortfolio(res: Response) {
    let body = res.json();
    var portfolio: Portfolio = new Portfolio();
    portfolio.email = body['email'];
    portfolio.username = body['name'];
    portfolio.id = parseInt(body['id']);
    return portfolio || {};
  }

  getPurchases(portfolioId) {
    return this.http.get(this.baseUrl + '/portfolio/' + portfolioId+ '/purchases')
      .map(this.mapPurchases)
      .catch(this.handleError);
  }

  private mapPurchases(res: Response) {
    let body = res.json();
    var purchases: Purchase[] = [];
    for (var purchase of body) {
      let pur = new Purchase();
      pur.id = parseInt(purchase['id']);
      pur.name = purchase['name'];
      pur.stock_id = purchase['stock_id'];
      pur.price = parseInt(purchase['price']);
      pur.volume = parseInt(purchase['volume']);
      purchases.push(pur);
    }
    return purchases || {};
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
