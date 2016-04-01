

exports = module.exports = createConfig;

/**
 * Simple config function
 */

function createConfig(options){

  var config = options || { };

  return function (obj, value){

    var copy;

    if( obj === void 0 || obj === null ){
      copy = merge({ }, config);
      return copy;
    }

    if( obj.clone ){
      delete obj.clone;
      copy = merge(config, obj);
      return createConfig(merge({ }, copy));
    } else if( obj.fork ){
      delete obj.fork;
      return createConfig(merge(config, obj));
    }

    if( Object(obj) !== obj ){
      return value ? config[obj] = value : config[obj];
    } else
      merge(config, obj);

    return this;
  };
}

/**
 * headless jaredhanson's merge
 * https://github.com/jaredhanson/utils-merge
 */
var merge = function(a, b){
  if (a && b) {
    for (var key in b) {
      a[key] = b[key];
    }
  }
  return a;
};
