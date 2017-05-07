/* tslint:disable:no-unused-variable */

import { TestBed, async, inject } from '@angular/core/testing';
import { FsmaService } from './fsma.service';

describe('FsmaService', () => {
  beforeEach(() => {
    TestBed.configureTestingModule({
      providers: [FsmaService]
    });
  });

  it('should ...', inject([FsmaService], (service: FsmaService) => {
    expect(service).toBeTruthy();
  }));
});
