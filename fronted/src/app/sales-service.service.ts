import { Injectable } from '@angular/core';
import { HttpClient, HttpErrorResponse } from '@angular/common/http';
import { Observable, throwError } from 'rxjs';
import { catchError } from 'rxjs/operators';


@Injectable({
  providedIn: 'root'
})

export class SalesService {
  private salesUrl = 'api/sales/sales.json';

  constructor(private http: HttpClient) { }


  private handleError(err: HttpErrorResponse){
    return throwError(`An error occurred: ${err}`);
  }
}