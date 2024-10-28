import { NgIf } from '@angular/common';
import { Component } from '@angular/core';
import { FormBuilder, FormGroup, ReactiveFormsModule, Validators } from '@angular/forms';

@Component({
  selector: 'app-generate-persona',
  standalone: true,
  imports: [NgIf, ReactiveFormsModule ],
  templateUrl: './generate-persona.component.html',
  styleUrl: './generate-persona.component.scss'
})
export class GeneratePersonaComponent  {
  loading: boolean = false;
  form: FormGroup;

  constructor(private fb: FormBuilder){ 
    this.form = this.fb.group({
      prompt: ['', [Validators.required, Validators.minLength(10)]],
      personaCount: [1, [Validators.required, Validators.min(1)]]
    });
  }

  toggleLoading() {
    this.loading = !this.loading;
  }

  onSubmit() {
    if (this.form.valid) {
      console.log('Form Submitted!', this.form.value);
    } else {
      console.log('Form is invalid');
    }
  }
}
