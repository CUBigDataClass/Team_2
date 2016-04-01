[<img alt="NPM version" src="http://img.shields.io/npm/v/utils-config.svg?style=flat-square" align="right"/>](http://www.npmjs.org/package/utils-config)

# utils-config

lazy object maintenance

## install

    $ npm install utils-config

## usage

```js
var config = require('utils-config');
var proto = {};
var init = {
  hey : 'want something'
}

proto.config = config(init);
proto.config();
// { hey : 'want something'}

proto.config('hey', 'not any more');
// 'not any more'

proto.config().hey = 'come on!'
// 'come on!'

proto.config();
// { hey : 'not any more'}

var clone = proto.config({ clone : true });
var fork  = proto.config({ fork : true });

fork('hey', 'ok, continue');
// 'ok, continue'
fork('hey');
// 'ok, continue'

proto.config();
// { hey : 'ok, continue' }

clone();
// { hey : 'not anymore' }
```

## license

[<img alt="LICENSE" src="http://img.shields.io/npm/l/utils-config.svg?style=flat-square"/>](http://opensource.org/licenses/MIT)
