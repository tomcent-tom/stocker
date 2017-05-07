/* tslint:disable:no-unused-variable */

import { TestBed, async, inject } from '@angular/core/testing';
import { SdatabaseService } from './sdb.service';

describe('SdatabaseService', () => {
  beforeEach(() => {
    TestBed.configureTestingModule({
      providers: [SdatabaseService]
    });
  });

  it('should ...', inject([SdatabaseService], (service: SdatabaseService) => {
    expect(service).toBeTruthy();
  }));
});
