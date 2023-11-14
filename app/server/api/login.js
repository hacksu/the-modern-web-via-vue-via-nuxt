import { findUserWithUsername } from '../data.js';

export default defineEventHandler(async (event) => {
  const body = await readBody(event);
  console.log('received request with body:', body);
  const existing = findUserWithUsername(body.username);
  if (!existing) {
    return false;
  } else if (existing.password == body.password) {
    console.log('password matched, returning true');
    // not secure, but:
    setCookie(event, 'username', existing.username);
    return true;
  } else {
    console.log("password didn't match, returning false");
    return false;
  }
});
