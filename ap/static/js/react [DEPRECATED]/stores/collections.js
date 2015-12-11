var Events = Backbone.Collection.extend({
  url: '/drf/events',
	model: Event
});
var Rolls = Backbone.Collection.extend({
  url: '/drf/rolls',
	model: Roll
});

var Slips = Backbone.Collection.extend({
  url: '/drf/leaveslips',
  model: Roll
});