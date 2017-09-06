require([
  'jquery',
  'mockup-patterns-modal',
], function($, Modal){
  'use strict';

      $('#content-core > a').each(function() {
      var modal = new Modal($(this), {
        width: '770px',
        height: '430px',

      });
      modal.on('after-render', function(e){
          $('.form-widgets-title').val('ciccio')
      })
    }); 

});
