<?php
/**
 * Al Rahal Auto Maintenance — Site Configuration
 * Edit ONLY this file to change business details across every page.
 */
define('SITE_NAME',      'Al Rahal Auto Maintenance');
define('SITE_SHORT',     'Al Rahal');
define('SITE_TAGLINE',   'Range Rover & Land Rover Specialists');
define('SITE_URL',       'https://www.alrahalauto.com');   // <-- change to your live domain (no trailing slash)

define('PHONE_DISPLAY',  '055 747 9292');
define('PHONE_INTL',     '971557479292');                   // international format, digits only
define('WA_BASE',        'https://wa.me/' . PHONE_INTL);
define('EMAIL',          'info@alrahalauto.com');           // <-- change

define('CITY',           'Dubai');                          // <-- change if needed
define('COUNTRY',        'United Arab Emirates');
define('ADDRESS_LINE',   'Al Quoz Industrial Area 3');      // <-- change
define('MAP_EMBED',      'https://www.google.com/maps?q=Al+Quoz+Industrial+Area+3+Dubai&output=embed'); // <-- your Google Maps embed URL
define('GEO_LAT',        '25.1290');
define('GEO_LNG',        '55.2270');

define('HOURS_DISPLAY',  'Saturday – Thursday, 8:00 AM – 8:00 PM');
define('HOURS_SCHEMA',   'Sa-Th 08:00-20:00');
define('FOUNDED_YEAR',   '2009');

define('GA_ID',          '');   // e.g. G-XXXXXXXXXX (Google Analytics 4) — blank = disabled
define('GSC_VERIFY',     '');   // Google Search Console verification token — blank = disabled

define('SOCIAL', [
  'instagram' => 'https://instagram.com/alrahalauto',
  'facebook'  => 'https://facebook.com/alrahalauto',
  'tiktok'    => 'https://tiktok.com/@alrahalauto',
]);

define('ASSET_VER', '1.0.0'); // bump after CSS/JS edits to refresh browser caches
