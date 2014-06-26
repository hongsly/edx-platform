/**
 * XBlockPublisher is a view that supports the following:
 * 1) Publishing of a draft version of an xblock.
 * 2) Discarding of edits in a draft version.
 * 3) Display of who last edited the xblock, and when.
 * 4) Display of publish status (published, published with changes, changes with no published version).
 */
define(["jquery", "gettext", "js/views/baseview"],
    function ($, gettext, BaseView) {
        'use strict';
        var XBlockPublisher = BaseView.extend({
            events: {
                'click .publish-button': 'publish',
                'click .discard-changes-button': 'discardChanges'
            },

            // takes XBlockInfo as a model

            initialize: function () {
                BaseView.prototype.initialize.call(this);
                this.template = this.loadTemplate('publish-xblock');
            },

            render: function () {
                this.$el.html(this.template({
                    has_changes: this.model.get('has_changes'),
                    published: this.model.get('published'),
                    edited_on: this.model.get('edited_on'),
                    edited_by: this.model.get('edited_by')
                }));

                return this;
            },

            publish: function (e) {
                if (e && e.preventDefault) {
                    e.preventDefault();
                }
                console.log('publish');
            },

            discardChanges: function (e) {
                if (e && e.preventDefault) {
                    e.preventDefault();
                }
                console.log('discard changes');
            }
        });

        return XBlockPublisher;
    }); // end define();