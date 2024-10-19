import { NgIf } from '@angular/common';
import { Component } from '@angular/core';

@Component({
  selector: 'app-generate-persona',
  standalone: true,
  imports: [NgIf],
  templateUrl: './generate-persona.component.html',
  styleUrl: './generate-persona.component.scss'
})
export class GeneratePersonaComponent {
  loading: boolean = false;

  toggleLoading() {
    this.loading = !this.loading;
  }
}
