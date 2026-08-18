#!/usr/bin/env python3
"""Build the Caleb Ulku / Automated SEO Workshop swipe site.

Run: python3 build_site.py
"""
import sys, os, glob
sys.path.insert(0, os.path.expanduser("~/scripts/_swipe_builder"))
from swipebuild import build

REPO = os.path.dirname(os.path.abspath(__file__))
PKG = os.path.expanduser("~/Downloads/CALEB_ULKU_Swipe")

tx = sorted(glob.glob(os.path.join(PKG, "Transcript", "0*.md")))

CONFIG = {
    "SITE": "Caleb Ulku — Automated SEO Workshop",
    "CREATOR": "Caleb Ulku",
    "FUNNEL_IDS": ["F126"],
    "CAPTURED": "6 August 2026",
    "REPO": REPO,
    "PACKAGE": "~/Downloads/CALEB_ULKU_Swipe",
    "BLURB": "A free-live-class funnel selling an AI local-SEO system to agency owners. "
             "Not our market. Swiped for one mechanic: the thank-you page that tells you your "
             "registration is <b>not complete</b> until you fill in a survey &mdash; then pays "
             "you a cheat sheet for finishing it and sells you a $49 upgrade on the other side.",

    "PAGES": [
        ("index.html", "Overview"),
        ("analysis.html", "Analysis"),
        ("pages.html", "Pages"),
        ("copybank.html", "Copy bank"),
        ("transcripts.html", "Transcripts"),
        ("videos.html", "Video library"),
        ("board.html", "Board"),
    ],

    "STATS": [
        ("Front end", "Free"),
        ("Upsell", "$49 VIP"),
        ("VIP anchor", "$197/mo"),
        ("Community", "$27/mo"),
        ("Skool members", "3,211"),
        ("Live ads", "~9 of 160"),
        ("Distinct ad copy", "1"),
        ("Phone required", "Yes"),
        ("Class length", "75 min"),
        ("Video captured", "8m 26s"),
    ],

    "OFFER": [
        ("Product", "Automated SEO Workshop &mdash; a free 75-minute live Zoom class"),
        ("Lead claim", "&ldquo;The AI Agent SEO System That Ranks Local Businesses in 14 Days "
                       "With Only 1 Hour of Work&rdquo;"),
        ("Mechanism", "<b>The Core 30</b> &mdash; entity-based site architecture (30 service "
                      "pages mirroring the Google Business Profile) plus an AI agent that runs "
                      "60 hours of fulfilment in one 90-minute session"),
        ("Big idea", "AI is absorbing informational search, but <b>AI can't fix a sink</b>. "
                     "Local service queries are the one category it cannot take, so local SEO "
                     "is worth more now, not less."),
        ("Front-end", "Free live class, Zoom, 1:00 PM ET, 75 minutes including Q&amp;A"),
        ("Upsell", "<b>$49 VIP</b> &mdash; day-2 live audit session (capped at 100), a "
                   "<b>7-day free trial of his own AI SEO software</b>, lifetime recording, "
                   "priority Q&amp;A"),
        ("Anchor for the upsell", "&ldquo;to get this kind of access to me normally you'd have "
                                  "to be inside my pro community, and that runs <b>$197 a "
                                  "month</b>&rdquo;"),
        ("Continuity", "Skool &mdash; <b>AI SEO Mastery</b>, $27/month, 3,211 members, 8 "
                       "courses, 288 modules, 6,154 posts"),
        ("Community guarantee", "&ldquo;Risk-free for 7 days. Pay $27 today &mdash; decide "
                                "later.&rdquo; No-questions refund inside a week."),
        ("Done-for-you", "calebulku.com/hire-my-agency &rarr; a GoHighLevel intake form on "
                         "<code>core30digital.com</code>"),
        ("Class price", '<span class="tag warn">not observed</span> &mdash; the paid offer is '
                        'pitched inside the live class, which we did not attend'),
        ("Proof strategy", "A <b>live demo</b> as the central promise: <i>&ldquo;Either it works "
                           "or it doesn't. You don't have to take anyone's word for it.&rdquo;</i>"),
    ],

    "FINDINGS": [
        ("The survey gate is the thing to steal",
         "The thank-you page does not thank you. The video opens <i>&ldquo;congratulations on "
         "registering and securing your spot &hellip; <b>but do not close this page yet because "
         "your registration isn't quite complete</b>&rdquo;</i>, then makes a sub-one-minute "
         "survey the thing that completes it: <i>&ldquo;it's only once you've submitted the "
         "survey that your spot will be fully confirmed.&rdquo;</i> The stated reason is "
         "generous &mdash; he wants to tailor the class to the room. The bribe is concrete: "
         "<i>&ldquo;as a thank you for filling it out, I'm going to send you my 14-day local SEO "
         "ranking cheat sheet.&rdquo;</i> One screen buys him a second micro-commitment, four "
         "segmentation fields, and a legitimate reason to email. <b>Show rate is our keystone "
         "metric and this is a working answer to it.</b>"),
        ("The $49 upsell is disclosed on the registration page, before it appears",
         "FAQ item five is written as the prospect's own words: <i>&ldquo;Is this free? What's "
         "the catch?&rdquo;</i> The answer names the upsell outright &mdash; <i>&ldquo;there's a "
         "$49 VIP upgrade available if you want lifetime recordings and extended access, but "
         "it's entirely optional.&rdquo;</i> Pre-disclosing the OTO costs nothing and removes "
         "the bait-and-switch feeling when it lands. Every other funnel in this swipe file "
         "hides it."),
        ("The price anchor is real and checkable, not invented",
         "<i>&ldquo;To get this kind of access to me normally, you'd have to be inside my pro "
         "community, and that runs $197 a month. But today, you're not paying $197. You're not "
         "even paying $100. Right here on this page, you can get the full VIP experience for "
         "just $49.&rdquo;</i> A three-step descent from a recurring price the prospect can go "
         "and verify, rather than a fabricated &ldquo;$2,000 value&rdquo;. Compare Shelby's "
         "invented $6,000 coach."),
        ("A product trial inside a $49 ticket",
         "VIP does not just buy attention, it buys the software: <i>&ldquo;I'll give you full "
         "access for seven days to use it on a real client. If it doesn't deliver, then cancel, "
         "no drama.&rdquo;</i> The buyer is inside the tool before the class runs, which turns "
         "the class into a product demo instead of a pitch. Product-led growth bolted onto a "
         "webinar funnel."),
        ("Two confirmation videos, one for buyers and one for everyone else",
         "The Wistia library holds <code>VSL/CONFIRMATION</code> (1m56s, includes the VIP tease) "
         "and <code>VIPCONFIRMATION</code> (1m00s, the identical script with the VIP paragraphs "
         "cut). Buyers do not get re-pitched what they already own. It cost him one re-cut and "
         "almost nobody bothers to do it."),
        ("One body copy, nine hooks — copy is settled, hooks are the test",
         "All ~9 live ads run <b>identical</b> body copy and the identical headline "
         "(&ldquo;Free Live Class: The New Way to Rank on Google&rdquo;). Only the 27&ndash;56 "
         "second video varies. Eight launched on 4 August, one on 6 August. The same body copy "
         "appears on inactive ads dating back to 17 June, so it has survived roughly seven weeks "
         "unchanged across 160 total ads. Survival rate live is <b>~9 of 160 (5.6%)</b>. "
         "<span class=\"tag warn\">n=12</span> of the inactive set was read in full; those "
         "carried 1&ndash;9 ads per creative, which is Andromeda-style re-upload rather than "
         "fresh writing."),
        ("The whole ad argument is one sentence",
         "<i>&ldquo;AI can't replace a real plumber. It can't fix a sink or install an HVAC "
         "system. So when someone searches for a local service, Google still has to show real "
         "local businesses.&rdquo;</i> The threat everyone else in the space is selling (AI is "
         "eating search) is reframed as the reason his niche is safe. A defensive market fact "
         "turned into an offensive positioning claim."),
        ("Proof by demonstration, not by testimonial",
         "The central promise is a live build: <i>&ldquo;watch the AI agent rank a real business "
         "in a single session &hellip; 60 hours of work, executed in one session.&rdquo;</i> The "
         "objection block leans on it too &mdash; <i>&ldquo;not a pre-recorded case study "
         "someone cleaned up before you saw it &hellip; either it works or it doesn't.&rdquo;</i> "
         "Three 23&ndash;49 second student testimonials sit on the page but they are support, "
         "not the argument."),
        ("The origin story leads with a failure and a domestic detail",
         "Six headline beats. The hook is not a number: <i>&ldquo;my wife and I were working so "
         "much we had to hire someone just to pick our son up before daycare locked the "
         "doors.&rdquo;</i> The first beat after quitting is getting a $3,000/month client's "
         "site de-indexed and being fired on the spot. Then $300,000 spent on training, the "
         "2023 pivot to local, 97 clients in six months, two 7-figure agencies."),
        ("Five required fields, including a phone number, for a free class",
         "First name, last name, email, <b>phone (required)</b>, plus a required consent box "
         "covering <b>both SMS and marketing email</b>. That is real friction on a cold Meta "
         "click and he is paying it on purpose &mdash; the number is what makes an SMS reminder "
         "layer possible. We did not submit it: there is no research phone number and "
         "fabricating one routes real calls to a real stranger."),
        ("The scarcity furniture is broken on a live cold page",
         "The sticky header reads <b>&ldquo;234 FREE Spots Left. Closing in 00D : 00H : 00M : "
         "00S&rdquo;</b>. The spot count is hardcoded and never decrements; the countdown is "
         "frozen at zero &mdash; re-rendered four seconds apart, the digits were identical. The "
         "event date is hardcoded eight times in the markup, and the cold ad was still serving "
         "at 3pm ET on 6 August, two hours after the 1pm class had ended. Somebody is buying "
         "clicks onto a dead timer."),
        ("Built on Lovable, not a funnel builder",
         "The og:image sits on <code>storage.googleapis.com/gpt-engineer-file-uploads</code>, "
         "the analytics file is <code>~flock.js</code>, and the markup is Tailwind with Sentry "
         "bolted on. This is a vibe-coded page, not ClickFunnels or GoHighLevel. Form is Tally "
         "in a modal, video is Wistia, tracking is Meta pixel <code>26795566503388851</code> "
         "plus a Google Ads tag &mdash; so they buy Google as well as Meta."),
        ("The back end was recovered without opting in",
         "The registration page preloads three downstream Wistia media by jsonp before you have "
         "given it anything: <code>VSL/CONFIRMATION</code>, <code>VIP</code> and "
         "<code>VIPCONFIRMATION</code>. All three were pulled at native quality and transcribed. "
         "The entire post-opt-in sequence &mdash; survey gate, $49 pitch, price anchor, bonus "
         "stack, scarcity cap &mdash; is documented here from a funnel we never entered. "
         "Worth checking on our own pages."),
    ],

    "FUNNEL": [
        ("Meta cold ad", "9 live, one body copy",
         "&ldquo;AI just changed how Google works&rdquo;. 27&ndash;56s video. "
         "&rarr; <code>events.calebulku.com</code>"),
        ("Registration page", "events.calebulku.com",
         "Long-form dark/gold. 20 CTA buttons, all identical. Lovable-built. "
         "Sticky countdown header, sticky footer CTA."),
        ("Opt-in", "tally.so/embed/NpvN4N",
         "Modal. First name, last name, email, <b>phone (required)</b>, SMS+email consent. "
         '<span class="tag warn">not submitted</span>'),
        ("Thank-you / confirmation", "not rendered &mdash; video recovered",
         "&ldquo;Your registration isn't quite complete.&rdquo; Survey gate, bribed with a "
         "14-day ranking cheat sheet."),
        ("Survey", "not rendered &mdash; questions from the video",
         "Where you're at, what clients, are you a local business, biggest local-SEO challenge."),
        ("$49 VIP OTO", "not rendered &mdash; 3m52s pitch recovered",
         "Day-2 audit session capped at 100, 7-day software trial, lifetime recording, "
         "priority Q&amp;A. Anchored against $197/mo."),
        ("Live class", "Zoom, 75 minutes",
         '<span class="tag good">dated, not evergreen</span> &mdash; the date is hardcoded in '
         'the markup, and the class had already ended while the ad was still serving.'),
        ("Skool community", "skool.com/ai-seo-mastery",
         "<b>$27/month</b>, 3,211 members, 8 courses, 288 modules."),
        ("Agency", "calebulku.com/hire-my-agency",
         "Done-for-you. GoHighLevel intake on <code>core30digital.com</code>."),
    ],

    "TRANSCRIPT_GROUPS": [("Captured video", tx)],
    "SLIDE_PAGES": [],

    "VIDEOS": [
        ("05_vip_oto_pitch.mp4", 232, "565 MB",
         "The $49 VIP pitch. Price anchor, four-bonus stack, 100-seat cap, software trial."),
        ("04_thankyou_confirmation_vsl.mp4", 116, "284 MB",
         "Thank-you page video. The survey gate and the cheat-sheet bribe."),
        ("06_vip_confirmation.mp4", 60, "132 MB",
         "Post-purchase re-cut of the confirmation video with the VIP pitch removed."),
        ("01_testimonial_shelby.mp4", 49, "77 MB",
         "Registration-page testimonial. &ldquo;Within two days I had my first client.&rdquo;"),
        ("02_testimonial_chad.mp4", 27, "35 MB",
         "Registration-page testimonial. Best value of any training he has done."),
        ("03_testimonial_steven.mp4", 22, "43 MB",
         "Registration-page testimonial. &ldquo;Just commit to the process and show up.&rdquo;"),
    ],

    "ANALYSIS": """
<div class="note"><b>The finding that matters.</b> Everything downstream of this opt-in was
recovered <i>without opting in</i>. The registration page preloads its own thank-you video, its
$49 upsell video and its post-purchase video by jsonp, before the visitor has typed anything. The
survey gate, the price anchor, the bonus stack and the scarcity cap are all documented here from
a funnel we never entered. Two implications: this is a repeatable capture technique for any
Wistia-backed funnel, and <b>our own pages should be checked for the same leak</b>.</div>

<h2 class="sec">Worth taking</h2>
<div class="grid g2">
<div class="card"><h3>The survey gate</h3><p>&ldquo;Your registration isn't quite complete.&rdquo;
A sub-one-minute survey framed as the thing that confirms the seat, paid for with a cheat sheet
delivered by email. It buys a second commitment, four segmentation fields and a reason to email
&mdash; on the screen where we currently say &ldquo;thanks, see you there.&rdquo; This is the
single most transferable thing in the swipe, and it points straight at our show-rate
bottleneck.</p></div>
<div class="card"><h3>Disclose the upsell before it appears</h3><p>The registration FAQ names the
$49 VIP in the prospect's own words &mdash; &ldquo;Is this free? What's the catch?&rdquo; &mdash;
so the OTO lands as a documented option rather than a surprise. Costs one paragraph.</p></div>
<div class="card"><h3>Anchor against a real recurring price</h3><p>$197/month for the pro
community, stepped down to $49 once, on a page where the prospect could go and check the $197.
An anchor that survives verification beats a bigger anchor that doesn't.</p></div>
<div class="card"><h3>Re-cut the confirmation video for buyers</h3><p>Two versions of the same
script, one with the pitch and one without, so buyers are not sold something they already own.
One afternoon of editing.</p></div>
<div class="card"><h3>Proof by live demonstration</h3><p>&ldquo;Not a pre-recorded case study
someone cleaned up before you saw it &hellip; either it works or it doesn't.&rdquo; He makes the
absence of editing the proof. Our equivalent would be building something live on a call rather
than showing the result of having built it.</p></div>
<div class="card"><h3>Reframe the category threat as the moat</h3><p>Everyone in his space is
scared AI is eating search. His one-sentence answer &mdash; &ldquo;AI can't fix a sink&rdquo;
&mdash; converts the industry's biggest fear into the reason his niche is the safe one. It has
carried every ad unchanged for seven weeks.</p></div>
</div>

<h2 class="sec">Read carefully</h2>
<p><b>The scarcity is dead furniture.</b> &ldquo;234 FREE Spots Left. Closing in 00D : 00H : 00M :
00S.&rdquo; The count is hardcoded and the timer is frozen at zero &mdash; verified by rendering
the page twice four seconds apart and comparing digits. The event date is hardcoded eight times,
and the cold ad was still serving two hours after the class ended. Someone is paying Meta to send
people to a page whose urgency device visibly does not work. Worth remembering that a broken
timer is worse than no timer: it tells the visitor nobody is minding the funnel.</p>
<p><b>The ad numbers are directional.</b> ~9 live of ~160 all-time is a 5.6% survival rate, but
that is an all-time denominator and it is not age-controlled &mdash; a June ad is inactive
because it is old, not because it lost. All nine live ads were read in full. Of the inactive set,
<b>n=12</b> were read; those showed 1&ndash;9 ads bundled per creative. The bundling read is
directional, not established.</p>
<p><b>Two claims are checkable and two are not.</b> The $1M+ Upwork earnings and the 3,211 Skool
members can be verified from source. &ldquo;200+ businesses ranked in the top 3&rdquo; and
&ldquo;97 clients in six months&rdquo; cannot be checked from outside and carry no disclosed
methodology. The earnings disclaimer is present and standard.</p>
<p><b>What we did not get.</b> The class itself, the paid offer and its price, the email sequence,
and the rendered thank-you / survey / OTO pages. All of it sits behind an opt-in that requires a
phone number, and we do not fabricate phone numbers &mdash; a made-up number routes a real
sales call to a real stranger. If Will wants the class and the email machine, the way in is a
real number he is willing to have texted.</p>
""",
}

if __name__ == "__main__":
    build(CONFIG)
