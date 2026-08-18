#!/usr/bin/env python3
"""Caleb Ulku — Automated SEO Workshop. The whole business, wired.

Run: python3 build_board.py  ->  board.html
"""
import sys, os
sys.path.insert(0, os.path.expanduser("~/scripts/_swipe_builder"))
from boardbuild import build, X

REPO = os.path.dirname(os.path.abspath(__file__))
S = os.path.expanduser("~/UNDERGROUND_FUNNELS_SSOT/01_RAW_FUNNELS")
W = f"{S}/Caleb_Ulku - Automated_SEO_Workshop - 2026-08-06/02_Pages"

CONFIG = {
    "OUT": os.path.join(REPO, "board.html"),
    "KICK": "Competitor swipe · captured 6 August 2026",
    "TITLE": "Caleb Ulku — the whole business, wired",
    "BLURB": "A free-live-class funnel for local SEO agencies. Not our market &mdash; swiped "
             "for its <b>mechanics</b>. The one worth stealing is the "
             "<b>survey gate</b>: the thank-you page tells you your registration is "
             "<i>not complete</i> until you answer five questions, bribes you with a cheat "
             "sheet for doing it, and drops a $49 upsell on the other side. That is a show-rate "
             "device, a segmentation engine and a self-liquidator in one screen.",

    "SHOTS": {
        "reg": {
            "col": 2, "y": 120, "lane": "event", "step": "Entry",
            "title": "Registration page",
            "url": "events.calebulku.com",
            "img": f"{W}/01_Webinar_registration/20260806T210000Z__screenshot_fullpage.png",
            "max_h": 1400,
            "note": "&ldquo;The AI Agent SEO System That Ranks Local Businesses in 14 Days With "
                    "Only 1 Hour of Work.&rdquo; Long-form, dark/gold, <b>20 CTA buttons</b>, all "
                    "the same. Built on <b>Lovable</b>, not ClickFunnels. Sticky header countdown, "
                    "sticky footer CTA.",
        },
        "form": {
            "col": 3, "y": 120, "lane": "event", "step": "Opt-in",
            "title": "Tally form, in a modal",
            "url": "tally.so/embed/NpvN4N",
            "img": f"{W}/03_Optin_form_Tally/20260806T203000Z__screenshot_fullpage.png",
            "max_h": 900,
            "note": "First name, last name, email, <b>phone (required)</b>, and a required "
                    "consent box for <b>SMS and email</b>. Five required fields for a free "
                    "class. Not submitted &mdash; we have no research phone number.",
        },
        "skool": {
            "col": 9, "y": 120, "lane": "back", "step": "Back end",
            "title": "Skool — AI SEO Mastery",
            "url": "skool.com/ai-seo-mastery",
            "img": f"{W}/05_Skool_community_BACK_END/20260806T202513Z__screenshot_fullpage.png",
            "max_h": 900,
            "note": "<b>$27/month</b>, 3,211 members, 8 courses, 288 modules, 6,154 posts. "
                    "&ldquo;Risk-free for 7 days. Pay $27 today &mdash; decide later.&rdquo;",
        },
        "agency": {
            "col": 10, "y": 120, "lane": "back", "step": "Done-for-you",
            "title": "Hire the agency",
            "url": "calebulku.com/hire-my-agency",
            "img": f"{W}/04_Agency_site/20260806T202456Z__screenshot_fullpage.png",
            "max_h": 900,
            "note": "&ldquo;Work 1-on-1 with the team behind Caleb's 7-figure AI SEO agency.&rdquo; "
                    "Intake is a GoHighLevel form on <code>core30digital.com</code> &mdash; a "
                    "separate entity from the education brand.",
        },
    },

    "DATA": {
        "ads": {
            "col": 1, "y": 120, "lane": "paid", "step": "Traffic",
            "title": "Meta cold — 9 live ads",
            "kv": [("All-time", "160 ads"),
                   ("Live now", "~9 (5.6%)"),
                   ("Distinct body copy", "<b>1</b>"),
                   ("Distinct headline", "<b>1</b>"),
                   ("Video lengths", "27&ndash;56s"),
                   ("Launched", "8 on Aug 4, 1 on Aug 6"),
                   ("Page name", "AI SEO Mastery"),
                   ("Also buying", "Google Ads (AW-417647429)")],
            "note": "Every live ad runs the <b>same</b> body copy and the <b>same</b> headline "
                    "(&ldquo;Free Live Class: The New Way to Rank on Google&rdquo;). Only the "
                    "video hook changes. The body has survived unchanged since at least 17 June.",
        },
        "ty": {
            "col": 4, "y": 120, "lane": "event", "step": "Thank-you",
            "title": "&ldquo;Your registration isn't complete&rdquo;",
            "kv": [("Video", "1m56s, Wistia"),
                   ("Claim", "spot not confirmed yet"),
                   ("Ask", "a &lt;1 min survey"),
                   ("Bribe", "14-Day Ranking Cheat Sheet"),
                   ("Delivery", "emailed after submit"),
                   ("Framing", "&ldquo;this is not pre-recorded&rdquo;")],
            "note": "<b>The single best mechanic in this funnel.</b> He does not say &ldquo;thanks, "
                    "see you there.&rdquo; He says the registration is incomplete, then makes the "
                    "survey the thing that completes it &mdash; and pays you a cheat sheet for "
                    "finishing. Compliance dressed as confirmation.",
        },
        "survey": {
            "col": 5, "y": 120, "lane": "event", "step": "Segmentation",
            "title": "The survey",
            "kv": [("Q", "where are you at right now"),
                   ("Q", "what clients are you working with"),
                   ("Q", "are you a local business"),
                   ("Q", "biggest local-SEO challenge"),
                   ("Stated reason", "&ldquo;tailor the class to the room&rdquo;"),
                   ("Real function", "segment + qualify + commit")],
            "note": "Questions recovered from the confirmation VSL, not from the page &mdash; the "
                    "opt-in demands a phone number so we never rendered it. Sold as a favour to "
                    "the attendee; it is a second micro-commitment and a lead-scoring input.",
        },
        "oto": {
            "col": 6, "y": 120, "lane": "back", "step": "Upsell",
            "title": "$49 VIP experience",
            "kv": [("Price", "<b>$49</b>"),
                   ("Anchor", "&ldquo;pro community &hellip; $197/month&rdquo;"),
                   ("Step-down", "not $197, not even $100, $49"),
                   ("Bonus 1", "day-2 live audit session"),
                   ("Scarcity", "first 100 VIPs only"),
                   ("Bonus 2", "<b>7-day free trial of his software</b>"),
                   ("Bonus 3", "lifetime recording"),
                   ("Bonus 4", "priority Q&amp;A"),
                   ("Pitch", "3m52s video")],
            "note": "Two-price framing, not a discount: the same access normally costs $197/mo, "
                    "today it is $49 once. The software trial is the real hook &mdash; it puts a "
                    "product in the buyer's hands before the class has even happened.",
        },
        "vipconf": {
            "col": 7, "y": 120, "lane": "back", "step": "Post-purchase",
            "title": "VIP confirmation",
            "kv": [("Video", "1m00s"),
                   ("Content", "same script, VIP block cut"),
                   ("Still asks for", "the survey"),
                   ("Still bribes with", "the cheat sheet")],
            "note": "A re-cut of the same confirmation video with the upsell paragraphs removed, "
                    "so buyers do not get re-pitched something they already own. Cheap to make, "
                    "and almost nobody bothers.",
        },
        "class": {
            "col": 8, "y": 120, "lane": "event", "step": "The pitch",
            "title": "Free live class",
            "kv": [("When", "Aug 6, 1:00 PM ET"),
                   ("Length", "75 minutes"),
                   ("Platform", "Zoom"),
                   ("Core promise", "<b>live demo on a real business</b>"),
                   ("Q&amp;A", "live attendees only"),
                   ("Replay", "limited for free, lifetime for VIP"),
                   ("Price pitched", "not observed")],
            "note": "The whole proof strategy is one line: <i>&ldquo;Either it works or it "
                    "doesn't. You don't have to take anyone's word for it.&rdquo;</i> The demo "
                    "IS the proof &mdash; not a testimonial wall, not a screenshot.",
        },
        "claims": {
            "col": 2, "y": 1560, "lane": "event", "step": "Proof claims",
            "title": "The numbers on the page",
            "kv": [("Agencies built", "2, both 7-figure"),
                   ("Businesses ranked top 3", "200+"),
                   ("Students", "2,000+ in 47 countries"),
                   ("Skool members", "3,211"),
                   ("Upwork earnings", "$1M+ verified"),
                   ("Spent on training", "$300,000"),
                   ("Clients in 6 months", "97"),
                   ("Credential", "Forbes Business Council"),
                   ("Credential", "MBA, Chicago Booth"),
                   ("Prior life", "10 years at ExxonMobil")],
            "note": "Two claims here are auditable and two are not. Upwork earnings and Skool "
                    "membership can be checked. &ldquo;200+ ranked top 3&rdquo; and &ldquo;97 "
                    "clients in 6 months&rdquo; cannot.",
        },
        "story": {
            "col": 4, "y": 1560, "lane": "event", "step": "Origin story",
            "title": "Six headline beats",
            "kv": [("1", "I had a safe career"),
                   ("2", "I quit and started an agency"),
                   ("3", "I spent $300,000 learning"),
                   ("4", "AI came, I went all in on local"),
                   ("5", "I automated it and hit 7 figures"),
                   ("6", "now it's my life's mission")],
            "note": "The hook is a detail, not a number: <i>&ldquo;we had to hire someone just to "
                    "pick our son up before daycare locked the doors.&rdquo;</i> And the first "
                    "beat after quitting is a <b>failure</b> &mdash; he got a client's site "
                    "de-indexed and was fired on the spot.",
        },
        "faq": {
            "col": 6, "y": 1560, "lane": "event", "step": "Objections",
            "title": "Seven objections, in quote marks",
            "kv": [("1", "burned by SEO gurus before"),
                   ("2", "never done SEO, can't code"),
                   ("3", "no time"),
                   ("4", "tried SEO, no results"),
                   ("5", "<b>is this free? what's the catch?</b>"),
                   ("6", "will it work for my niche"),
                   ("7", "will there be a replay")],
            "note": "Written as the prospect's own words in quotation marks, not as neutral FAQ "
                    "headings. Objection 5 <b>pre-discloses the $49 upsell on the registration "
                    "page</b>, so the OTO cannot read as bait-and-switch when it appears.",
        },
    },

    "EDGES": [
        ("ads", "reg"), ("reg", "form"), ("form", "ty"), ("ty", "survey"),
        ("survey", "oto"), ("oto", "vipconf"), ("vipconf", "class"),
        ("class", "skool"), ("skool", "agency"),
    ],

    "LABELS": [
        {"x": X[1], "y": 60, "t": "The funnel"},
        {"x": X[1], "y": 1500, "t": "What the page argues"},
        {"x": X[1], "y": 2760, "t": "Routing logic and reads"},
    ],

    "BRANCH": [
        {"id": "b_survey", "x": X[1] + 10, "y": 2820, "state": "yes",
         "cond": "Opts in → told the registration is NOT complete",
         "body": "<i>&ldquo;Congratulations on registering and securing your spot &hellip; but do "
                 "not close this page yet because your registration isn't quite complete &hellip; "
                 "it's only once you've submitted the survey that your spot will be fully "
                 "confirmed.&rdquo;</i> Then: <i>&ldquo;as a thank you for filling it out, I'm "
                 "going to send you my 14-day local SEO ranking cheat sheet.&rdquo;</i> "
                 "<b>Show rate is our keystone metric and this is a working answer to it</b> "
                 "&mdash; a second commitment, a segmentation payload and a lead-magnet delivery "
                 "reason to email, all bought with one screen.",
         "ev": "VERIFIED · confirmation VSL transcribed 6 Aug (04_thankyou_confirmation_vsl.md)"},
        {"id": "b_oto", "x": X[3] + 10, "y": 2820, "state": "yes",
         "cond": "Completes the survey → $49 VIP page",
         "body": "The anchor is not a fake retail price, it is a <b>real recurring one</b>: "
                 "<i>&ldquo;to get this kind of access to me normally, you'd have to be inside my "
                 "pro community, and that runs $197 a month. But today you're not paying $197. "
                 "You're not even paying $100. Right here on this page you can get the full VIP "
                 "experience for just $49.&rdquo;</i> A three-step descent from a price the "
                 "prospect can verify. Scarcity is capped at the first 100 and tied to a real "
                 "constraint &mdash; he can only go deep on so many websites live.",
         "ev": "VERIFIED · OTO video transcribed 6 Aug (05_vip_oto_pitch.md)"},
        {"id": "b_trial", "x": X[5] + 10, "y": 2820, "state": "yes",
         "cond": "Buys VIP → 7-day trial of his own software",
         "body": "The $49 does not just buy attention, it buys a <b>product trial</b>: "
                 "<i>&ldquo;I'll give you full access for seven days to use it on a real client. "
                 "If it doesn't deliver, cancel, no drama.&rdquo;</i> Product-led growth bolted "
                 "onto a webinar funnel. The buyer is inside the tool before the class has even "
                 "run, which makes the class a product demo rather than a pitch.",
         "ev": "VERIFIED · OTO video transcribed 6 Aug"},
        {"id": "b_phone", "x": X[7] + 10, "y": 2820, "state": "unver",
         "cond": "Phone is required for a free class",
         "body": "Five required fields including a mobile number and a combined <b>SMS + email</b> "
                 "consent box. That is real friction on a cold Meta click, and he is paying it "
                 "deliberately &mdash; the number is what makes an SMS reminder layer possible. "
                 "Whether the trade is worth it is exactly the test we should be running on our "
                 "own opt-in, in both directions.",
         "ev": "VERIFIED as required · not submitted, no research phone number exists"},
        {"id": "b_broken", "x": X[9] + 10, "y": 2820, "state": "dq",
         "cond": "The scarcity furniture is dead on a live cold page",
         "body": "The sticky header reads <b>&ldquo;234 FREE Spots Left. Closing in "
                 "00D : 00H : 00M : 00S&rdquo;</b> and does not move. The number is hardcoded and "
                 "never decrements; the countdown is frozen at zero. The event date "
                 "&ldquo;August 6 @ 1:00 PM ET&rdquo; is hardcoded eight times in the markup, and "
                 "the cold ad was still serving at 3pm ET on 6 August &mdash; after the class had "
                 "already ended. Somebody is paying for clicks onto a dead timer.",
         "ev": "VERIFIED · re-rendered twice 4 seconds apart, digits identical"},
        {"id": "b_ads", "x": X[11] + 10, "y": 2820, "state": "yes",
         "cond": "One body copy, nine hooks",
         "body": "All ~9 live ads carry <b>identical</b> body copy and an identical headline; only "
                 "the 27&ndash;56 second video varies. The body has run unchanged since at least "
                 "17 June across 160 total ads. They are not testing copy &mdash; copy is settled. "
                 "They are testing <b>hooks</b>, and they re-upload the winner rather than "
                 "rewriting it. The argument itself is one sentence: <i>AI can't fix a sink</i>, "
                 "so local service search is the one category AI cannot absorb.",
         "ev": "VERIFIED · Meta Ad Library, 9 live cards read in full 6 Aug; ~160 all-time"},
    ],

    "LEGEND": [("paid", "Paid traffic"), ("event", "Free class route"),
               ("back", "$49 VIP + $27/mo + agency")],
}

if __name__ == "__main__":
    build(CONFIG)
