import { index2 } from '@Components';
import mocha from 'mocha';
import { createName, FullName } from './createname';
import { index1 } from './component/x.component';
import * as crossSpawn from 'cross-spawn';
import 'rxjs/operators/map';
import React, { useState, useCallback } from 'react';
import { x1 } from './component';

// Cases:
// React: useState useCallback
// in {x1} add x2

export class Greeter<T> {
	greeting: T;
	constructor(message: T) {
		this.greeting = message;
	}
	greet() {
		return this.greeting;
	}
}

export let greeter = new Greeter<string>('Hello, world');

let button = document.createElement('button');
button.textContent = 'Say Hello';
button.onclick = function () {
	alert(greeter.greet());
};
// createName FullName index1 index2 worker_threads mocha fs readFileSync copyFileSync
// `cross-spawn` mocha Animal Snake Horse
document.body.appendChild(button);
// HTTP_STATUS_CONTINUE
function foo(res) {
	res.json(typeof HTTP2_HEADER_STATUS);
}

export const $goo = 1;
export const goo$ = 2;
